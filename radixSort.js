var data = [0, 5, 100, 1000, 75, 3, 44, 3490, 23, 4, 435, 123, 49, 403, 2498]

function getDigit(num, place, base = 10) {
	let value = 0
	while (place) {
		value = num % base
		num = Math.floor((num - value) / base)
		place--
	}
	return value
}

function radixSort(arr, base = 10) {
	let maxDigits = Math.floor(Math.log10(Math.max(...arr))) + 1

	for ( let num = 1; num <= maxDigits; num++) {
		// make buckets
		let buckets = [];
		let index = 0

		for (let bucket = 0; bucket < base; bucket++) {
			buckets.push([])
		}
		// iterate over array
		arr.forEach( number => {
			// get digit in the 1s,10s,100s, etc place
			let digit = getDigit(number, num)
			// push number into appropriate bucket
			buckets[digit].push(number)
		})
		console.log(buckets);

		// ternary to push non-empty buckets back into arr
		buckets.forEach((bucket) => {
			bucket ? bucket.forEach( value => {
				arr[index] = value
				index++
			}) : null
		})
	}

	return arr
}

// let digit = getDigit(1234, 7)
// console.log(digit)

console.log(radixSort(data));