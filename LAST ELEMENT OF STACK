#include <iostream>
#include <stack>

using namespace std;

int findLastElement(stack<int>& s) {
    if (s.empty()) {
        return -1; 
    }
    int top = s.top();
    s.pop();
    if (s.empty()) {
        s.push(top);
        return top;
    }
    int lastElement = findLastElement(s);
    s.push(top);
    return lastElement;
}

int main() {
    stack<int> myStack;
    myStack.push(80);
    myStack.push(20);
    myStack.push(30);

    int lastElement = findLastElement(myStack);

    if (lastElement != -1) {
        cout << "Last element of the stack: " << lastElement << endl;
    } else {
        cout << "Stack is empty." << endl;
    }

    return 0;
}
