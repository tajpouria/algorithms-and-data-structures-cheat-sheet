interface INode {
    value: any;
    priority: number;
}

class _Node implements INode {
    constructor(public value: any, public priority: number = 0) {}
}

class PriorityQueue {
    private _values: INode[] = [];
    get values(): INode[] {
        return this._values;
    }

    private sinkingUp(node: INode): void {
        let valueIndex = this._values.length - 1;
        while (valueIndex > 0) {
            const parentIndex = Math.floor((valueIndex - 1) / 2);
            const parent = this._values[parentIndex];

            if (node.priority >= parent.priority) break;

            this._values[parentIndex] = node;
            this._values[valueIndex] = parent;

            valueIndex = parentIndex;
        }
    }
    private sinkingDown(): void {
        let targetIndex = 0;
        while (true) {
            let leftChildIndex = targetIndex * 2 + 1,
                rightChildIndex = targetIndex * 2 + 2;

            let target = this._values[targetIndex],
                leftChild = this._values[leftChildIndex],
                rightChild = this._values[rightChildIndex];

            if (
                leftChild &&
                rightChild &&
                target.priority > leftChild.priority &&
                target.priority > rightChild.priority
            ) {
                if (rightChild.priority < leftChild.priority) {
                    [
                        this._values[targetIndex],
                        this._values[rightChildIndex]
                    ] = [
                        this._values[rightChildIndex],
                        this._values[targetIndex]
                    ];

                    targetIndex = rightChildIndex;
                } else {
                    [
                        this._values[targetIndex],
                        this._values[leftChildIndex]
                    ] = [
                        this._values[leftChildIndex],
                        this._values[targetIndex]
                    ];

                    targetIndex = leftChildIndex;
                }

                continue;
            } else if (rightChild && rightChild.priority <= target.priority) {
                [this._values[targetIndex], this._values[rightChildIndex]] = [
                    this._values[rightChildIndex],
                    this._values[targetIndex]
                ];

                targetIndex = leftChildIndex;

                continue;
            } else if (leftChild && leftChild.priority <= target.priority) {
                [this._values[targetIndex], this._values[leftChildIndex]] = [
                    this._values[leftChildIndex],
                    this._values[targetIndex]
                ];

                targetIndex = leftChildIndex;

                continue;
            }

            break;
        }
    }

    public enqueue({ value, priority }: INode): _Node[] {
        const node = new _Node(value, priority);
        this._values.push(node);
        this.sinkingUp(node);
        return this._values;
    }

    public dequeue(): _Node | null {
        if (!this._values.length) {
            return null;
        }
        const root = this._values[0];
        this._values[0] = this._values[this._values.length - 1];
        this._values.pop();
        this.sinkingDown();

        return root;
    }
}

const heap = new PriorityQueue();
const arr: INode[] = [
    { value: 1, priority: 0 },
    { value: 3, priority: 4 },
    { value: 5, priority: 2 },
    { value: 8, priority: -1 },
    { value: 4, priority: 5 }
];

arr.forEach((el: INode) => heap.enqueue(el));

heap.dequeue();
heap.dequeue();

heap.enqueue({ value: "GOOZ", priority: 40 });

console.log(heap.values);
