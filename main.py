from year import Year
from locations import Locations
from sweepstakes import Sweepstakes
from family import Family
from linkedlist import LinkedList
from treenode import Treenode


if __name__ == '__main__':
    #Problem 1A (Tuple)
    year = Year(2021)
    year.find_pie()

    #Problem 1B (Set)
    locations = Locations()
    locations.future_locations('Bahamas')
    locations.future_locations('Cancun')
    locations.future_locations('Scotland')
    locations.show_locations()

    #Problem 1C (Dictionary)
    sweepstakes = Sweepstakes()
    sweepstakes.winner()

    #Problem 2 (Dict of family members)
    family = Family()
    family.show_family()

    #Problem 3 (Linked List)
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)

    linked_list.add_to_beginning(100)
    linked_list.contains_node(55)

    #Problem 4 (Binary Tree)
    tree = Treenode(100)
    tree = tree.insert(tree, 90)
    tree = tree.insert(tree, 95)
    tree = tree.insert(tree, 80)
    tree = tree.insert(tree, 85)
    tree = tree.insert(tree, 70)
    tree = tree.insert(tree, 75)
    tree = tree.insert(tree, 60)
    tree = tree.insert(tree, 65)

    tree.search_for_node(tree, 100)
    tree.search_for_node(tree, 95)
    tree.search_for_node(tree, 99)

    tree.in_order(tree)
