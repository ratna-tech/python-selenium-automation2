Feature: Test Scenarios for Search functionality

  Scenario: # Search for candy
    Given Open Target page
    When search for jeans
    When add item to cart
    Then verify jeans in cart

Scenario: # Search for airpods
    Given Open Target page
    When search for airpods
    When add item to cart
    Then verify airpods in cart

Scenario: User can select colors
    #Given Open target product A-54551690 page
    Given Open target product A-91667868 page
    Then Verify user can click hrough colors


Scenario: Search product has a name and image
    Given Open Target page
    When search for mugs
    Then verify product has a name
    Then verify product has image

