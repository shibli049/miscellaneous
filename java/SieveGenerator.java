/**
 * A memory optimized sieve generator.
 */

public class SieveGenerator {
    private MyBitSet sieve;
    public static final int MAX_RANGE = 2146483646;
    int range = MAX_RANGE;
    
    
    public SieveGenerator(int range){
        if(range > MAX_RANGE){
             throw new IndexOutOfBoundsException(String.format("range > {0} : {1}", MAX_RANGE, range));
        }        
        this.range = range;
    }
    
    public void generate() {        
        sieve = new MyBitSet(range);        
        sieve.set(0, true);
        sieve.set(1, true);        
        for (int i = 4; i < range; i += 2) {
            sieve.set(i, true);
        }
        
        int len = (int) Math.sqrt(range) + 2;
        for (int i = 3; i < len; i += 2) {
            if (!sieve.get(i)) {
                for (int j = i * i; j < range; j += (i+i)) {
                    sieve.set(j, true);
                }
            }
        }
    }

    public MyBitSet getSieve() {
        return sieve;
    }
    
    
    public boolean isPrime(int i){
        return !sieve.get(i);
    }
}

// this class is a simplified version of java.util.BitSet
class MyBitSet {

        private long[] words;
        private final static int ADDRESS_BITS_PER_WORD = 6;
        private transient int wordsInUse = 0;

        public MyBitSet(int nbits) {            
            words = new long[wordIndex(nbits-1) + 1];
            wordsInUse = words.length;
        }

        private int wordIndex(int bitIndex) {
            return bitIndex >> ADDRESS_BITS_PER_WORD;
        }

        private void  clear(int bitIndex) {
            int wordIndex = wordIndex(bitIndex);
            if (wordIndex >= wordsInUse) {
                return;
            }
            words[wordIndex] &= ~(1L << bitIndex);

        }

        private void set(int bitIndex) {
            int wordIndex = wordIndex(bitIndex);
            words[wordIndex] |= (1L << bitIndex);
        }
        
        public void set(int bitIndex, boolean value) {
            if(value){
                set(bitIndex);
            }else{
                clear(bitIndex);
            }
        }

        public boolean get(int bitIndex) {                        
            int wordIndex = wordIndex(bitIndex);
            return (wordIndex < wordsInUse)
                    && ((words[wordIndex] & (1L << bitIndex)) != 0);
        }
    }