Feature: Search in Google
  In order to test google search
  As a user
  I want to search something and get a result

  Scenario: Positive search
    Given I go to "http://www.google.com.au/"
    When I fill in "q" with "test"
    Then I should see results

  Scenario: Negative search
    Given I go to "http://www.google.com.au/"
    When I fill in "q" with "aj;lsdkfjajksdljf;a"
    Then I should see no results