/*
Add a method to a linked list to insert a node at the given position. Pass in two arguments, node value and insert position.

For example:

ll = LinkedList()

ll.extend([1, 2, 3, 4, 5, 6])


ll.insert(4,2)


The list would then have nodes ordered like this: 1,2,4,3,4,5,6

For the above example, it would be valid to insert an item at index 6. Inserting an item at an index equal to the list's length is the same as appending a new item to the list. Additionally, it is valid to insert an item at index 0, which puts that item at the head of the list. Make sure to account for these edge cases in your code.


** pseudocode **

Linked List class
    Head pointer
    Node struct?
        next pointer
        prev pointer
        data
    node count
    

    Methods
        list constructor
            Head pointer
        list destructor
            delete pointers
        node constructor
        node destructor
        insert node
        delete node
        count nodes
        isEmpty

    

*/
namespace linkedList {

class LinkedList {
    private:
    public:
        LinkedList(); //Constructor
        int* create_node(int value);
        int


LinkedList::LinkedList() {
    cout << "Default LinkedList Constructor" << endl;
}

LinkedList::~LinkedList() {
    cout << "LinkedList Destructor" << endl;
}



}






} // End linkedList namespace.

