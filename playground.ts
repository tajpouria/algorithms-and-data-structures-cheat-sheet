type El = [string, any];
class HashTable {
    private keyMap: El[][];
    constructor(size: number = 53) {
        this.keyMap = new Array(size);
    }

    public _hash(key: string): number {
        let total = 0;
        const WEIRD_PRIME = 31;

        for (let i = 0; i < key.length; i++) {
            const characterCode = key.charCodeAt(i) - 96;
            total = (total + characterCode * WEIRD_PRIME) % this.keyMap.length;
        }
        return total;
    }

    set(key: string, value: any): El[][] {
        const index = this._hash(key);
        if (!this.keyMap[index]) {
            this.keyMap[index] = [];
        }

        this.keyMap[index].push([key, value]);

        return this.keyMap;
    }

    get(key: string): El | undefined {
        const index = this._hash(key);

        const elements = this.keyMap[index];

        if (elements) {
            for (let value of elements) {
                if (value[0] === key) return value[1];
            }
        }

        return undefined;
    }

    get keys(): string[] {
        const keys: string[] = [];
        for (let value of this.keyMap) {
            if (value) {
                for (let _value of value) {
                    keys.push(_value[0]);
                }
            }
        }
        return keys;
    }

    get values(): any[] {
        const values = new Set<any>();

        for (let value of this.keyMap) {
            if (value) {
                for (let _value of value) {
                    values.add(value[1]);
                }
            }
        }

        return [...values];
    }
}
