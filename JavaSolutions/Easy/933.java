package Easy;
import java.util.LinkedList;
import java.util.Queue;
// Use of an interface such as Queue<T> for the requests.
// Reference: https://docs.oracle.com/javase/8/docs/api/java/util/Queue.html
// Reference for LinkedList : https://docs.oracle.com/javase/8/docs/api/java/util/LinkedList.html

class RecentCounter {
    // Use of an interface such as Queue<T> for the requests
    Queue<Integer> requests;  

    public RecentCounter() {
        // Use of a concrete class (LinkedList) to implement the queue
        requests = new LinkedList<>();
    }

    public int ping(int t) {
        // Add the new ping to the LinkedList
        requests.offer(t); // In a Queue interface, it's better to use offer() rather than add()
        
        // Since every ping is larger than the previous one, the head is the first one to be checked
        while (requests.peek() < t - 3000) {
            // If the timestamp is not in the range [t - 3000, t], it needs to be removed 
            requests.poll();
        }
        
        // Return the total number of requests that happened within the last time frame
        return requests.size();
    }
}