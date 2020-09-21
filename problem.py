from pulp import *


def main():
    """Create problems, solve & display."""
    # Define variables
    x1 = pulp.LpVariable("x1", lowBound=0)
    x2 = pulp.LpVariable("x2", lowBound=0)

    # Create system of linear equations
    sys_eq = [
            (2 * x1 + 4 * x2, "Target function"),
            (5 * x1 + 8 * x2 <= 40, "1"),
            (7 * x1 + 5 * x2 <= 35, "2"),
            (x1 + x2 >= 2, "3"),
            (x1 - x2 <= 3, "4"),
            (-x1 + x2 <= 4, "5")
        ]

    # Create problems (maximizing and minimizing)
    max_prob = pulp.LpProblem("0", LpMaximize)
    min_prob = pulp.LpProblem("0", LpMinimize)

    # Get result
    max_res = solve_problem(max_prob, sys_eq)
    min_res = solve_problem(min_prob, sys_eq)

    # Display results
    print("=" * 50)
    print(f"Maximum of target function:\n\t{max_res['obj']}")
    print(f"Variables:\n\t"
          f"x1 = {max_res['x1']}\n\t"
          f"x2 = {max_res['x2']}")

    print("=" * 50)
    print(f"Minimum of target function:\n\t{min_res['obj']}")
    print(f"Variables:\n\t"
          f"x1 = {min_res['x1']}\n\t"
          f"x2 = {min_res['x2']}")
    print("=" * 50)


def solve_problem(problem, sys_eq: list) -> dict:
    """Fill & solve problem.

    Problem is a system of linear equations with target function.
    """
    # Fills problem
    for eq in sys_eq:
        problem += eq

    # Solve and save results in dict
    problem.solve()
    res = {}
    for variable in problem.variables():
        res[variable.name] = [variable.varValue]
    res["obj"] = value(problem.objective)

    return res


if __name__ == "__main__":
    main()
