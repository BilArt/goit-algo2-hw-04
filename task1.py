from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")
        
        count = 0
        for word in self.get_all_words():
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix: str) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")
        
        return bool(self.find(prefix))

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
    
    print("All tests passed!")
