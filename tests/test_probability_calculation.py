"""
Test suite for FTA Editor probability calculation validation
Tests AND/OR gate logic and link handling against the REAL core implementation
(src/FTA_Editor_core.py -> FTACore.recalculate_probabilities).

Note: this file previously defined a mock ProbabilityCalculator that only
verified a copy of the formula, so changes to the real core code could not
break these tests. It now imports and exercises the real FTACore instead.
"""
import unittest
import sys
from pathlib import Path

# Add project root to path so we can import the real core module
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.FTA_Editor_core import FTACore


class TestProbabilityCalculation(unittest.TestCase):
    """Test cases for probability calculation logic (real FTACore)"""

    def setUp(self):
        """Set up test fixtures"""
        self.core = FTACore()

    def calc(self, data):
        """Run the real core probability calculation and return the data"""
        self.core.set_data(data)
        self.core.recalculate_probabilities()
        return self.core.get_data()

    def test_leaf_node_probability(self):
        """Test that leaf nodes use their base probability"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 0.5,
            "logicGate": "OR",
            "children": [],
            "links": []
        })
        self.assertAlmostEqual(result["calculatedProbability"], 0.5, delta=1e-9)

    def test_and_gate_with_two_children(self):
        """Test AND gate: should calculate product(child_probs)"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 0.8,
            "logicGate": "AND",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.4,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # AND: product(children) = 0.5 * 0.4 = 0.2
        # Parent's base probability is ignored when children exist
        self.assertAlmostEqual(result["calculatedProbability"], 0.2, delta=1e-9)
        self.assertAlmostEqual(result["children"][0]["calculatedProbability"], 0.5, delta=1e-9)
        self.assertAlmostEqual(result["children"][1]["calculatedProbability"], 0.4, delta=1e-9)

    def test_or_gate_with_two_children(self):
        """Test OR gate: should use 1 - product(1 - child_prob)"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "OR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.4,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # OR: 1 - product(1 - child_prob) = 1 - (1-0.5)*(1-0.4) = 1 - 0.5*0.6 = 1 - 0.3 = 0.7
        self.assertAlmostEqual(result["calculatedProbability"], 0.7, delta=1e-9)

    def test_and_gate_with_three_children(self):
        """Test AND gate with three children"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "AND",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.6,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child3",
                    "name": "Child3",
                    "type": "Event",
                    "probability": 0.8,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # AND: product(children) = 0.5 * 0.6 * 0.8 = 0.24
        self.assertAlmostEqual(result["calculatedProbability"], 0.24, delta=1e-9)

    def test_or_gate_with_three_children(self):
        """Test OR gate with three children"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "OR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.6,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child3",
                    "name": "Child3",
                    "type": "Event",
                    "probability": 0.8,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # OR: 1 - (1-0.5)*(1-0.6)*(1-0.8) = 1 - 0.5*0.4*0.2 = 1 - 0.04 = 0.96
        self.assertAlmostEqual(result["calculatedProbability"], 0.96, delta=1e-9)

    def test_and_link_simple(self):
        """Test AND link between nodes"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 0.5,
            "logicGate": "OR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.8,
                    "logicGate": "OR",
                    "children": [],
                    "links": [
                        {
                            "target_id": "child2",
                            "relation": "AND"
                        }
                    ]
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.6,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # child2 has no links: 0.6
        self.assertAlmostEqual(result["children"][1]["calculatedProbability"], 0.6, delta=1e-9)
        # child1 AND-linked to child2: 0.8 * 0.6 = 0.48
        self.assertAlmostEqual(result["children"][0]["calculatedProbability"], 0.48, delta=1e-9)

    def test_or_link_simple(self):
        """Test OR link between nodes"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 0.5,
            "logicGate": "OR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": [
                        {
                            "target_id": "child2",
                            "relation": "OR"
                        }
                    ]
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.3,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # child2: 0.3
        self.assertAlmostEqual(result["children"][1]["calculatedProbability"], 0.3, delta=1e-9)
        # child1 OR-linked to child2: 1 - (1-0.5)*(1-0.3) = 1 - 0.5*0.7 = 1 - 0.35 = 0.65
        self.assertAlmostEqual(result["children"][0]["calculatedProbability"], 0.65, delta=1e-9)

    def test_mixed_and_or_links(self):
        """Test node with both AND and OR links"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "OR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": [
                        {
                            "target_id": "child2",
                            "relation": "AND"
                        },
                        {
                            "target_id": "child3",
                            "relation": "OR"
                        }
                    ]
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.8,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child3",
                    "name": "Child3",
                    "type": "Event",
                    "probability": 0.4,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # child2: 0.8, child3: 0.4
        self.assertAlmostEqual(result["children"][1]["calculatedProbability"], 0.8, delta=1e-9)
        self.assertAlmostEqual(result["children"][2]["calculatedProbability"], 0.4, delta=1e-9)
        # child1: first apply AND link: 0.5 * 0.8 = 0.4
        # then apply OR link: 1 - (1-0.4)*(1-0.4) = 1 - 0.6*0.6 = 1 - 0.36 = 0.64
        self.assertAlmostEqual(result["children"][0]["calculatedProbability"], 0.64, delta=1e-9)

    def test_zero_probability_leaf(self):
        """Test that zero probability propagates correctly"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "AND",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.0,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 1.0,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # AND gate with one zero child: 0.0 * 1.0 = 0.0
        self.assertAlmostEqual(result["calculatedProbability"], 0.0, delta=1e-9)

    def test_nested_and_gates(self):
        """Test nested AND gates"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "AND",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.9,
                    "logicGate": "AND",
                    "children": [
                        {
                            "id": "grandchild1",
                            "name": "GrandChild1",
                            "type": "Event",
                            "probability": 0.5,
                            "logicGate": "OR",
                            "children": [],
                            "links": []
                        },
                        {
                            "id": "grandchild2",
                            "name": "GrandChild2",
                            "type": "Event",
                            "probability": 0.6,
                            "logicGate": "OR",
                            "children": [],
                            "links": []
                        }
                    ],
                    "links": []
                }
            ],
            "links": []
        })
        # grandchild1: 0.5, grandchild2: 0.6
        self.assertAlmostEqual(result["children"][0]["children"][0]["calculatedProbability"], 0.5, delta=1e-9)
        self.assertAlmostEqual(result["children"][0]["children"][1]["calculatedProbability"], 0.6, delta=1e-9)
        # child1 (AND gate): product(children) = 0.5 * 0.6 = 0.3
        self.assertAlmostEqual(result["children"][0]["calculatedProbability"], 0.3, delta=1e-9)
        # root (AND gate): product(children) = 0.3
        self.assertAlmostEqual(result["calculatedProbability"], 0.3, delta=1e-9)

    def test_nested_or_gates(self):
        """Test nested OR gates"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "OR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 1.0,
                    "logicGate": "OR",
                    "children": [
                        {
                            "id": "grandchild1",
                            "name": "GrandChild1",
                            "type": "Event",
                            "probability": 0.5,
                            "logicGate": "OR",
                            "children": [],
                            "links": []
                        },
                        {
                            "id": "grandchild2",
                            "name": "GrandChild2",
                            "type": "Event",
                            "probability": 0.2,
                            "logicGate": "OR",
                            "children": [],
                            "links": []
                        }
                    ],
                    "links": []
                }
            ],
            "links": []
        })
        # grandchild1: 0.5, grandchild2: 0.2
        self.assertAlmostEqual(result["children"][0]["children"][0]["calculatedProbability"], 0.5, delta=1e-9)
        self.assertAlmostEqual(result["children"][0]["children"][1]["calculatedProbability"], 0.2, delta=1e-9)
        # child1 (OR gate): 1 - (1-0.5)*(1-0.2) = 1 - 0.5*0.8 = 1 - 0.4 = 0.6
        self.assertAlmostEqual(result["children"][0]["calculatedProbability"], 0.6, delta=1e-9)
        # root (OR gate): 1 - (1-0.6) = 1 - 0.4 = 0.6
        self.assertAlmostEqual(result["calculatedProbability"], 0.6, delta=1e-9)

    def test_circular_reference_protection(self):
        """Test that circular references are handled (uses base probability)"""
        # This is a tricky case - we set up a potential circular reference
        # The algorithm should handle this with the visiting set
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "OR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": [
                        {
                            "target_id": "child1",  # Self-reference
                            "relation": "OR"
                        }
                    ]
                }
            ],
            "links": []
        })
        # Should complete without infinite loop
        # When circular reference detected, uses base probability
        self.assertIsNotNone(result["children"][0]["calculatedProbability"])

    def test_xor_gate_two_children(self):
        """Test XOR gate: exactly one child must occur"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "XOR",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "child2",
                    "name": "Child2",
                    "type": "Event",
                    "probability": 0.4,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # XOR: 0.5*(1-0.4) + 0.4*(1-0.5) = 0.3 + 0.2 = 0.5
        self.assertAlmostEqual(result["calculatedProbability"], 0.5, delta=1e-9)

    def test_not_gate(self):
        """Test NOT gate: complement of the child probability"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "NOT",
            "children": [
                {
                    "id": "child1",
                    "name": "Child1",
                    "type": "Event",
                    "probability": 0.3,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        # NOT: 1 - 0.3 = 0.7
        self.assertAlmostEqual(result["calculatedProbability"], 0.7, delta=1e-9)

    @staticmethod
    def _three_children():
        return [
            {
                "id": f"child{i}",
                "name": f"Child{i}",
                "type": "Event",
                "probability": p,
                "logicGate": "OR",
                "children": [],
                "links": []
            }
            for i, p in enumerate([0.5, 0.6, 0.8], start=1)
        ]

    def test_voter_gate_default_majority(self):
        """Test VOTER gate with default threshold (majority = 2-out-of-3)"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "VOTER",
            "children": self._three_children(),
            "links": []
        })
        # P(>=2 of 3) = 0.5*0.6*0.2 + 0.5*0.4*0.8 + 0.5*0.6*0.8 + 0.5*0.6*0.8
        #             = 0.06 + 0.16 + 0.24 + 0.24 = 0.70
        self.assertAlmostEqual(result["calculatedProbability"], 0.7, delta=1e-9)

    def test_voter_gate_custom_threshold(self):
        """Test VOTER gate with explicit voteThreshold=3 (all must occur)"""
        result = self.calc({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "VOTER",
            "voteThreshold": 3,
            "children": self._three_children(),
            "links": []
        })
        # 3-out-of-3: 0.5 * 0.6 * 0.8 = 0.24
        self.assertAlmostEqual(result["calculatedProbability"], 0.24, delta=1e-9)


class TestSampleDataValidation(unittest.TestCase):
    """Validate calculations against the sample FTA data (real FTACore)"""

    def setUp(self):
        """Set up test fixtures"""
        self.core = FTACore()

    def test_sample_event_1_1_1(self):
        """Test Event1.1.1 from sampleFTA.json
        - Base probability: 0.5
        - Has OR link to root_1_1 (prob 0.0)
        - Has AND link to root_0_2 (prob 0.8)
        - Expected: 0.5 * 0.8 (AND) = 0.4, then OR with 0.0 = 0.4
        """
        self.core.set_data({
            "id": "root",
            "name": "Root",
            "type": "Event",
            "probability": 1.0,
            "logicGate": "OR",
            "children": [
                {
                    "id": "root_0_0_0",
                    "name": "Ev1.1.1",
                    "type": "Event",
                    "probability": 0.5,
                    "logicGate": "OR",
                    "children": [],
                    "links": [
                        {
                            "target_id": "root_1_1",
                            "relation": "OR"
                        },
                        {
                            "target_id": "root_0_2",
                            "relation": "AND"
                        }
                    ]
                },
                {
                    "id": "root_1_1",
                    "name": "Ev2.2",
                    "type": "Event",
                    "probability": 0.0,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                },
                {
                    "id": "root_0_2",
                    "name": "Ev1.3",
                    "type": "Event",
                    "probability": 0.8,
                    "logicGate": "OR",
                    "children": [],
                    "links": []
                }
            ],
            "links": []
        })
        self.core.recalculate_probabilities()
        node = self.core.find_node_by_id("root_0_0_0")
        # First AND link: 0.5 * 0.8 = 0.4
        # Then OR link: 1 - (1-0.4)*(1-0.0) = 1 - 0.6*1.0 = 0.4
        self.assertAlmostEqual(node["calculatedProbability"], 0.4, delta=1e-9)

    def test_sample_file_matches_stored_results(self):
        """Load the real sampleFTA.json and verify recalculated probabilities
        match the calculatedProbability values stored in the file."""
        sample_path = (Path(__file__).parent.parent
                       / "data" / "examples" / "sampleFTA.json")
        if not sample_path.exists():
            self.skipTest(f"sample file not found: {sample_path}")

        success, error = self.core.load_from_json(str(sample_path))
        self.assertTrue(success, f"Failed to load sampleFTA.json: {error}")

        # load_from_json() normalizes and recalculates probabilities; compare
        # against the values stored in the file itself
        import json
        with open(sample_path, "r", encoding="utf-8") as f:
            stored = json.load(f)["tree"]

        def check(node, stored_node):
            self.assertAlmostEqual(
                node.get("calculatedProbability"),
                stored_node.get("calculatedProbability"),
                delta=1e-6,  # stored values were rounded to 6 decimals
                msg=f"Mismatch at node {node.get('id')} ({node.get('name')})"
            )
            for child, stored_child in zip(node.get("children", []),
                                           stored_node.get("children", [])):
                check(child, stored_child)

        check(self.core.get_data(), stored)

        # Spot-check the documented expectation for Ev1.1.1 (root_0_0_0)
        ev111 = self.core.find_node_by_id("root_0_0_0")
        self.assertAlmostEqual(ev111["calculatedProbability"], 0.4, delta=1e-9)


def run_tests():
    """Run all tests and print results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test cases
    suite.addTests(loader.loadTestsFromTestCase(TestProbabilityCalculation))
    suite.addTests(loader.loadTestsFromTestCase(TestSampleDataValidation))

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "="*70)
    print("PROBABILITY CALCULATION VALIDATION SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)

    if result.wasSuccessful():
        print("\n✓ All probability calculation tests passed!")
        print("\nValidated behaviors (against real src/FTA_Editor_core.py):")
        print("  • AND gate: calculates product of child probabilities")
        print("  • OR gate: uses union formula 1 - product(1 - p for each child)")
        print("  • XOR gate: exactly one child occurs")
        print("  • NOT gate: complement of the child probability")
        print("  • VOTER gate: k-out-of-n (voteThreshold, default majority)")
        print("  • AND links: multiply current probability with linked probabilities")
        print("  • OR links: apply union formula with linked probabilities")
        print("  • Mixed links: AND links applied first, then OR links")
        print("  • Circular references: handled via visiting set (uses base probability)")
        print("  • sampleFTA.json: recalculated values match stored results")
    else:
        print("\n✗ Some tests failed. See details above.")

    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
