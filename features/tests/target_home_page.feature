# Created by matth at 11/20/2023

Feature: Homework 6 test case

  Scenario: User can see cart is empty message
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown

#  Scenario: Logged out user can access Sign In
#    Given Open target main page
#    When Click Sign In
#    And From right side nav menu click Sign in
#    Then Verify Sign in form opens