class Node
  def initialize(data, next_node)
    @data = data
    @next_node = next_node
  end
end

class LinkedList
  def initialize(head)
    @head = nil
  end

  def add(data)
    node = Node.new(data)
    if @head == nil
      @head = node
    else
      current = @head
      while current != nil do
        current = current.next_node
      end
      current.next_node = node
    end
  end

  def delete(data)
    if @head == nil
      return false
    
  end

end