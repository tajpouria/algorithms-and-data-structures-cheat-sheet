## Big O Notation

### time complexity

it allow us to talk formally about how the runtime of an algorithm grows as the input grows.

n = number of operation the computer has to do can be:
f(n) = n
f(n) = n\*\*2
f(n) = 1

f(n) = could be something entirely different !

![](./assets/ece920b.png)

O(n):

```typescript
function addUpToSimple(n: number) {
    let total = 0;
    for (let i = 0; i < n; i++) {
        total += i;
    }
    return total;
}
```

O(1):

```typescript
function addUpComplex(n: number) {
    return (n * (n + 1)) / 2;
}
```

O(n): maybe thinking O(2n) but we see big picture! BigONotation doesn't care about precision only about general trends _linear? quadric? constant?_

```typescript
function printUpAndDown(n: number) {
    console.log("Going up");
    for (let i = 0; i < n; i++) {
        console.log(i);
    }
    console.log("Going down");
    for (let j = n - 1; j > 0; j--) {
        console.log(j);
    }
}
```

O(n\*\*2)

```typescript
function printAllPairs(n: number) {
    for (let i = 0; i < n; i++) {
        console.log(i);
        for (let j = 0; j < n; j++) {
            console.log(j);
        }
    }
}
```

O(n) : cuz as soon as n grows complexity grows too

```typescript
function logAtLeastFive(n: number) {
    for (let i = 0; i <= Math.max(5, n); i++) {
        console.log(i);
    }
}
```

O(1)

```typescript
function logAtMostFive(n: number) {
    for (let i = 0; i <= Math.min(5, n); i++) {
        console.log(i);
    }
}
```

### space complexity

Rules of Thumb

-   most primitive _booleans numbers undefined null_ are constant space.
-   strings and reference types like objects an arrays require O(n) space _n is string length or number of keys_

O(1)

```typescript
function sum(arr: number[]) {
    let total = 0;
    for (let i = 0; i < arr.length; i++) {
        total += arr[i];
    }
}
```

O(n)

```typescript
function double(arr: number[]) {
    const newArr = [];
    for (let i = 0; i < arr.length; i++) {
        array.push(arr[i] * 2);
    }
    return newArr;
}
```
