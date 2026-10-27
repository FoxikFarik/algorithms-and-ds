#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MinHeap {
private:
    vector<int> heap;

    void siftUp(int i) {
        while (i > 1) {
            int p = i / 2;
            if (heap[i] >= heap[p]) break;
            swap(heap[i], heap[p]);
            i = p;
        }
    }

    void siftDown(int i) {
        int n = (int)heap.size();
        while (true) {
            int l = 2 * i;
            int r = 2 * i + 1;
            int smallest = i;
            if (l < n && heap[l] < heap[smallest]) smallest = l;
            if (r < n && heap[r] < heap[smallest]) smallest = r;
            if (smallest == i) break;
            swap(heap[i], heap[smallest]);
            i = smallest;
        }
    }

public:
    MinHeap() { heap.push_back(0); }

    void clear() {
        heap.clear();
        heap.push_back(0);
    }

    void insert(int x) {
        heap.push_back(x);
        siftUp((int)heap.size() - 1);
    }

    int extract() {
        int el = heap[1];
        heap[1] = heap.back();
        heap.pop_back();
        if (heap.size() > 1) siftDown(1);
        return el;
    }

    bool isEmpty() const {
        return heap.size() == 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    MinHeap heap;
    string command;
    int x;

    while (cin >> command) {
        if (command == "CLEAR") {
            heap.clear();
        } else if (command == "ADD") {
            cin >> x;
            heap.insert(x);
        } else if (command == "EXTRACT") {
            if (heap.isEmpty())
                cout << "CANNOT" << endl;
            else
                cout << heap.extract() << endl;
        }
    }
    return 0;
}