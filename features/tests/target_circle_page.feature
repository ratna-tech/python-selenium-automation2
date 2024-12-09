# Created by ashva at 12/7/2024
Feature: Target circle page features
  # Enter feature description here

  Scenario: verify there are 14 benefit cells
    Given Open Target page
    Given Open target circle page
    When Click on the benefits cell
    Then verify 14 cells are present