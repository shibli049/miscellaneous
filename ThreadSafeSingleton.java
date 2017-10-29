// reference: https://www.ibm.com/developerworks/java/library/j-dcl/index.html
class ThreadSafeSingleton {
    private static ThreadSafeSingleton _instance = null;

    private ThreadSafeSingleton() {
    }

    public static ThreadSafeSingleton getInstance() {
        if (_instance == null) {
            synchronized (ThreadSafeSingleton.class) {
                if (_instance == null) {
                    ThreadSafeSingleton ins = new ThreadSafeSingleton();
                    _instance = ins;
                }
            }
        }
        return _instance;
    }

}