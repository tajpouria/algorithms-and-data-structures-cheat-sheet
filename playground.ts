function getDigit(num: number, i: number): number {
    return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
}

function digitCount(num: number): number {
    if (num === 0) return 1;
    return Math.floor(Math.log10(Math.abs(num))) + 1;
}

function mostDigits(arr: number[]): number {
    let maxDigits = 0;
    for (let i = 0; i < arr.length; i++) {
        maxDigits = Math.max(maxDigits, digitCount(arr[i]));
    }
    return maxDigits;
}

function radixSort(arr: number[]): number[] {
    let maxDigitCount = mostDigits(arr);
    for (let i = 0; i < maxDigitCount; i++) {
        let digitBuckets = Array.from({ length: 10 }, () => []);
        for (let j = 0; j < arr.length; j++) {
            digitBuckets[getDigit(arr[j], i)].push(arr[j]);
        }

        arr = [].concat(...digitBuckets);
    }
    return arr;
}
