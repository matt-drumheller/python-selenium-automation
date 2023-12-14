Feature: Tests for product page

#  Scenario: User can select colors
#    Given Open target product A-88062531 page
#    Then Verify user can click through colors
    
  Scenario: User is able to select different colors available for a product
    Given Open target product A-88345376 page
    When Select size small
    Then Verify user can click through colors