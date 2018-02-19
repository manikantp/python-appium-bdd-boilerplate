Feature: Reddit demo

  As a user
  I want to find a gaming subreddit
  So that I can talk about EA

  Background:
    Given the app is running

  Scenario: The time
    Given I open the app
    When I search for 'gaming'
    Then I see the gaming subreddit
