Feature: Calculator
    Validate basic arithmetic operation provided by the calculator

    Scenario: Addition
        Given the calculator is intialized
        When I add 10 and 5    
        Then the result should be 20

    Scenario: Subtraction
        Given the calculator is intialized
        When I subtract 10 and 5
        Then the result should be 5

    Scenario: Multiplication
        Given the calculator is intialized
        When I mutiply 10 and 5
        Then the result should be 50

    Scenario: Division
        Given the calculator is intialized
        When I divide 10 and 5
        Then the result should be 2

    Scenario: Calculate the cosine of a number
        Given the calculator is intialized
        When I calculate the cosine of 0
        Then the result should be 1

    Scenario: Calculate the sine of a number
        Given the calculator is intialized
        When I calculate the sine of 0
        Then the result should be 0

    Scenario: Calculate the tangent of a number
        Given the calculator is intialized
        When I calculate the tangent of 0
        Then the result should be 0

