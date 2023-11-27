# Created by matth at 11/19/2023
Feature: Search tests


  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    And Verify search result url