let arr = [2,5,3,6,4,2,6,3,8,5]


function merge(bottom, top) {
    console.log('merge', bottom, top)
    let smallest = 0
    if (top.length === 0 ) {
        return bottom
    } 
    if (bottom.length === 0) {
        return top
    }

    smallest = bottom[0] <= top[0] ? bottom.shift() : top.shift()

    let merged = merge(bottom, top)
    merged.unshift(smallest)
    console.log(merged)
    return merged

}

function mergeSort(arr) {
    if (arr.length <= 1) {
        console.log('base', arr)
        return arr
    }
    let middle = Math.ceil(arr.length / 2)
    // console.log('recurse', arr)
    topHalf = arr.slice(middle,arr.length);
    bottomHalf = arr.slice(0,middle);
    console.log(topHalf, bottomHalf)
    sortedTopHalf = mergeSort(topHalf)
    sortedBottomHalf = mergeSort(bottomHalf)
    
    return merge(sortedBottomHalf, sortedTopHalf)
}
    
mergeSort(arr);

