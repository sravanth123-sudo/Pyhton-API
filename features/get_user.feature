Feature: Get User API and validate from DB

  Scenario: Verify user details from API and database
    Given the user ID is 2
    When I send a GET request to the user endpoint
    Then the response status code should be 200
    And the response should match the data from database
