Feature: Main page UI tests

  Scenario: Header has correct amount of links
    Given Open target main page
    When Verify header is present
    Then Verify header has 5 links


  Scenario: Verify item can be added to cart
    Given Open target main page
    When Search for basketball
    And Add item to cart
    And Close pop up window
    And Click on cart icon
    Then Verify there is an item added to cart