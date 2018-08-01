let data = [0, 5, 100, 1000, 75, 3, 44, 3490, 23, 4, 435, 123, 49, 403, 2498]

function heapify(arr, heapSize, index) {
	let big = index;
	let left = 2 * index + 1;
	let right = 2 * index + 2;

	if (left < heapSize && arr[index] < arr[left]) {
		big = left;
	} 
	if (right < heapSize && arr[big] < arr[right]) {
		big = right;
	} 
	
	if (big !== index) {
		let tmp = arr[big]
		arr[big] = arr[index];
		arr[index] = tmp
		heapify(arr, heapSize, big);
	}
}

function heapSort(arr) {
	let heapSize = arr.length;

	for (let i = heapSize; i >= 0 ; i--) {
		console.log(arr);
		heapify(arr, heapSize, i);
	}

	for (let i = (heapSize - 1); i >= 1 ; i--) {
		let tmp = arr[0]
		arr[0] = arr[i];
		arr[i] = tmp
		console.log(arr);
		heapify(arr, i, 0)
	}

	return arr
}

heapSort(data);

