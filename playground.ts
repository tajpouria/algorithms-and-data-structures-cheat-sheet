class _Node {
    constructor(public value: any) {}
    public next: _Node | null = null;
}

class SinglyLinkedList {
    private _length: number = 0;
    private head: _Node | null = null;
    private tail: _Node | null = null;

    get length() {
        return this._length;
    }

    get print(): null | _Node[] {
        if (!this._length) return null;

        const arr = [];
        let currentNode = this.head;
        while (currentNode) {
            arr.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return arr;
    }

    public push(value: any): SinglyLinkedList {
        const node = new _Node(value);

        if (!this.head || !this.tail) {
            this.head = node;
            this.tail = this.head;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
        this._length += 1;

        return this;
    }

    public pop(): _Node | null {
        if (!this.head) return null;

        let currentNode = this.head;

        if (!currentNode.next) {
            this.head = null;
            this.tail = null;
            this._length -= 1;
            return currentNode;
        }
        while (currentNode.next && currentNode.next.next) {
            currentNode = currentNode.next;
        }
        this.tail = currentNode;
        this.tail.next = null;
        this._length -= 1;
        return currentNode.next as _Node;
    }

    public unShift(value: any): SinglyLinkedList {
        const currentHead = this.head;

        this.head = new _Node(value);

        if (currentHead) {
            this.head.next = currentHead;
        } else {
            this.tail = this.head;
        }
        this._length += 1;
        return this;
    }

    public shift(): _Node | null {
        if (!this.head) return null;

        const currentHead = this.head;
        this.head = currentHead.next;
        this._length -= 1;

        if (currentHead === this.tail) this.tail = null;

        return currentHead;
    }

    public get(index: number): _Node | null {
        if (index < 0 || index >= this._length) return null;

        let currentNode = this.head;
        for (let j = 0; j < index; j++) {
            if (currentNode && currentNode.next) {
                currentNode = currentNode.next;
            }
        }
        return currentNode;
    }

    public set(index: number, value: any): _Node | null {
        const node = this.get(index);
        if (node) {
            node.value = value;
        }
        return node;
    }

    public insert(index: number, value: any): SinglyLinkedList | null {
        if (index === 0) {
            return this.unShift(value);
        } else if (index === this._length) {
            return this.push(value);
        } else {
            const prevNode = this.get(index - 1);

            if (prevNode) {
                const newNode = new _Node(value);
                newNode.next = prevNode.next;
                prevNode.next = newNode;
                this._length += 1;

                return this;
            }
            return prevNode;
        }
    }

    public remove(index: number): _Node | null {
        if (index === 0) {
            return this.shift();
        } else if (index === this._length - 1) {
            return this.pop();
        } else {
            const prevNode = this.get(index - 1);
            const currentNode = this.get(index);
            if (prevNode && currentNode) {
                prevNode.next = currentNode.next;
                this._length -= 1;
            }
            return currentNode;
        }
    }

    public reverse(): SinglyLinkedList | false {
        if (this._length <= 1) return false;

        let node = this.head;
        this.head = this.tail;
        this.tail = node;

        let next: _Node | null;
        let prev: _Node | null = null;
        for (let i = 0; i < this._length; i++) {
            if (node) {
                next = node.next;
                node.next = prev;
                prev = node;
                node = next;
            }
        }
        return this;
    }
}
