# Created by matth at 11/19/2023
Feature: Search tests


  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search worked for coffee
    And Verify coffee in search result url

  Scenario: User can search for a tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea
    And Verify tea in search result url

  Scenario: User can search for a mug
    Given Open target main page
    When Search for mug
    Then Verify search worked for mug
    And Verify mug in search result url