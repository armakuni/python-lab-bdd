Feature: Posting messages
  As a social person
  I want to see a list of message from all the people I'm interested in
  So that I'm kept up to date with all the exciting things that they are doing

  # Rule: Users see messages they write themselves

  Scenario: The user sees their own messages
    Given Alice has posted a message "Hello fans"
    And Alice has posted a message "It's a lovely day today"
    When Alice views their feed
    Then they can see the message "Hello fans" by Alice
    And they can see the message "It's a lovely day today" by Alice

  # Rule: Users see messages written by people they follow

#  Scenario: The user doesn't see message from people they're not following
#    Given Bob has posted a message "Bob here"
#    And Alice is not following Bob
#    When Alice views their feed
#    Then they cannot see the message "Bob here" by Bob
#
#  Scenario: The user sees a message from someone they follow
#    Given Bob has posted a message "Bob here again"
#    And Alice follows Bob
#    When Alice views their feed
#    Then they can see the message "Bob here again" by Bob

  # Rule: Users see messages which mention them

#  Scenario: The user has been mentioned in a message
#    Given Alice has posted a message "I like @Bob"
#    When Bob views their feed
#    Then they can see the message "I like @Bob" by Alice
#
#  Scenario: The user with a similar name has been mentioned
#    Given Alice has posted a message "I like @BobHope"
#    When Bob views their feed
#    Then they cannot see the message "I like @BobHope" by Alice
#
#  Scenario: The user is mentioned in the middle of a message
#    Given Alice has posted a message "I like @Bob a lot"
#    When Bob views their feed
#    Then they can see the message "I like @Bob a lot" by Alice
#
#  Scenario: The user mention is in a different case
#    Given Alice has posted a message "I like @bOb"
#    When Bob views their feed
#    Then they can see the message "I like @bOb" by Alice
#
#  Scenario: The user mention is not a separated word
#    Given Alice has posted a message "Ilike@Bob"
#    When Bob views their feed
#    Then they cannot see the message "Ilike@Bob" by Alice
