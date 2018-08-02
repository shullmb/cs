// Binary Tree

class TreeNode {
	constructor(data) {
		this.leftChild = null;
		this.rightChild = null;
		this.data = data;
	}
}

class BinarySearchTree {
	constructor() {
		this.root = null;
	}

	// insert a node with the provided data as a child of the provided node
	insert(node, data) {
		if (!this.root) {
			this.root = new TreeNode(data)
			return node;
		} else {
			if (data < node.data && !node.leftChild) {
				node.leftChild = new TreeNode(data);
			} else if (data < node.data) {
				node.leftChild = this.insert(node.leftChild, data);
			} else if (data > node.data && !node.rightChild) {
				node.rightChild = new TreeNode(data);
			} else if (data > node.data) {
				node.rightChild = this.insert(node.rightChild, data);
			}
			return node
		}
	}

	preOrderTraversal(node) {
		// root => left => right
		if (node) {
			console.log(" root: ", node.data); //print root
			console.log(" left: ", (node.leftChild ? node.leftChild.data : '-'));
			console.log("right: ", (node.rightChild ? node.rightChild.data : '-'));
			console.log("============================");

			if (node.leftChild) {
				this.preOrderTraversal(node.leftChild);
			}
			if (node.rightChild) {
				this.preOrderTraversal(node.rightChild)
			}
		}
	}

	inOrderFeed(node) {
		if (node) {
			let arr = [];
			// leftChild
			if (node.leftChild) {
				arr.push(...this.inOrderFeed(node.leftChild));
			}
			// root / current node
			arr.push(node.data);
			// rightChild
			if (node.rightChild) {
				arr.push(...this.inOrderFeed(node.rightChild));
			}
			return arr;
		}
	}

	emptyTree(node) {
		// Post Order: left => right => root
		if (node) {
			if (node.leftChild) {
				this.emptyTree(node.leftChild);
				node.leftChild = null
			}
			if (node.rightChild) {
				this.emptyTree(node.rightChild);
				node.rightChild = null
			}
			node.data = null;
		}
		this.root = null
	}

	buildTreeFromArray(arr) {
		if (arr.length <= 1) {
			this.insert(this.root, arr[0])
		} else {
			let mid = Math.floor(arr.length / 2);
			this.insert(this.root, arr[mid]);
			this.buildTreeFromArray(arr.slice(0, mid));
			this.buildTreeFromArray(arr.slice(mid + 1, arr.length));
		}
	}

	balance() {
		// feed tree data into arr
		let arr = this.inOrderFeed(this.root);
		// empty the tree
		this.emptyTree(this.root);
		// rebuild the tree in a more balanced way 
		this.buildTreeFromArray(arr);
	}
}

var bst = new BinarySearchTree();

bst.insert(bst.root, 5);
bst.insert(bst.root, 10);
bst.insert(bst.root, 15);
bst.insert(bst.root, 20);
bst.insert(bst.root, 25);
bst.insert(bst.root, 30);

console.log('><><><><><><><><><><><><><><');
console.log('Pre order');
console.log('><><><><><><><><><><><><><><');

bst.preOrderTraversal(bst.root);

bst.balance();

console.log('><><><><><><><><><><><><><><');
console.log('Balanced');
console.log('><><><><><><><><><><><><><><');
bst.preOrderTraversal(bst.root);

