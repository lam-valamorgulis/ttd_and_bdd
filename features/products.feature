Scenario: List all products
  When I request a list of products
  Then the response should contain a list of products
