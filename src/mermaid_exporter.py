# -*- coding: utf-8 -*-
"""
Export fault tree data to Mermaid flowchart text.

WPS Office and other tools can import a flowchart by pasting Mermaid text,
producing an editable diagram. This module renders the FTA/ETA tree as a
Mermaid `flowchart TD` with event boxes and AND/OR logic gate diamonds.
"""
import json
import sys

GATE_CN = {"OR": "或门", "AND": "与门", "XOR": "异或门", "NOT": "非门"}
DIRECTION = {"FTA": "TD", "ETA": "TD"}


def _label(name):
    return name.replace("\\", "\\\\").replace('"', '\\"')


def build_mermaid(tree, mode="FTA"):
    """Return Mermaid flowchart text for a fault/event tree."""
    lines = ["flowchart %s" % DIRECTION.get((mode or "").upper(), "TD"), ""]
    midmap = {}
    counter = [0]
    gate_counter = [0]

    def node_id(node):
        key = node.get("id")
        if key not in midmap:
            counter[0] += 1
            midmap[key] = "n%d" % counter[0]
        return midmap[key]

    def emit_node(node):
        mid = node_id(node)
        name = _label(node.get("name") or node.get("id") or "")
        lines.append('%s["%s"]' % (mid, name))

    # depth-first: emit definitions and connections
    def walk(node):
        mid = node_id(node)
        emit_node(node)
        children = node.get("children", []) or []
        if not children:
            return
        gate = (node.get("logicGate") or "").strip()
        if gate:
            gate_counter[0] += 1
            gid = "g%d" % gate_counter[0]
            gname = GATE_CN.get(gate.upper(), gate)
            lines.append('%s{"%s"}' % (gid, _label(gname)))
            lines.append("%s --> %s" % (mid, gid))
            for ch in children:
                cmid = node_id(ch)
                prob = ch.get("probability")
                edge = '-->|"%s"|' % _label(str(prob)) if prob not in (None, "", 0.0) else "-->"
                lines.append("%s %s %s" % (gid, edge, cmid))
        else:
            for ch in children:
                cmid = node_id(ch)
                prob = ch.get("probability")
                edge = '-->|"%s"|' % _label(str(prob)) if prob not in (None, "", 0.0) else "-->"
                lines.append("%s %s %s" % (mid, edge, cmid))
        for ch in children:
            walk(ch)

    walk(tree)
    return "\n".join(lines)


def export_to_mermaid(data):
    tree = data.get("tree") or data if isinstance(data, dict) else data
    if not isinstance(tree, dict):
        raise ValueError("无效的故障树数据")
    return build_mermaid(tree, data.get("mode", "FTA"))


def _main(argv):
    import argparse
    p = argparse.ArgumentParser(description="Export FTA data to Mermaid text")
    p.add_argument("-i", "--input", default="sample.json", help="input json (FTA export data)")
    p.add_argument("-o", "--output", default="out.mmd", help="output .mmd/.md path")
    args = p.parse_args(argv)
    with open(args.input, encoding="utf-8-sig") as f:
        data = json.load(f)
    text = export_to_mermaid(data)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    _main(sys.argv[1:])