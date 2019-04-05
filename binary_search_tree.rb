class TreeNode
  attr_accessor :left_child, :right_child, :data

  def initialize data, left_child = nil, right_child = nil
    @data = data
    @left_child = left_child
    @right_child = right_child
  end
end

class BinarySearchTree
  attr_accessor :root
  def initialize
    @root = nil
  end

  def insert node, data
    if !@root
      @root = TreeNode.new(data)
      return node
    else
      if data < node.data && !node.left_child
    end
  end

end

