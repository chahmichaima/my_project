class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0  
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    def total_pages(self):
        if len(self.items) == 0:
            return 1
        return (len(self.items) + self.page_size - 1) // self.page_size
    def go_to_page(self, page_num):
        target_idx = page_num - 1
        if 0 <= target_idx < self.total_pages():
            self.current_idx = target_idx
        else:
            print(f"Error: Page {page_num} is out of range. Page remains unchanged.")
        return self  
    def first_page(self):
        self.current_idx = 0
        return self
    def last_page(self):
        self.current_idx = self.total_pages() - 1
        return self
    def next_page(self):
        if self.current_idx < self.total_pages() - 1:
            self.current_idx += 1
        return self
    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
    def display_current_page(self):
        visible = self.get_visible_items()
        return "\n".join(str(item) for item in visible)
# ==========================================
# Step 6: (Test Cases )
# ==========================================
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)
    print("--- 1. اes elements visible 1er page ---")
    print(p.get_visible_items())  
    print("\n--- 2eme page  s--")
    p.next_page()
    print(p.get_visible_items()) 
    print("\n--- 3eme pages directement ---")
    p.last_page()
    print(p.get_visible_items())  

    print("\n--- 4.7---")
    p.go_to_page(7)
    print(p.current_idx + 1)  
    print("\n--- 5.teste ---")
    p.go_to_page(60)  
    print("\n--- 6 Display Current Page ---")
    p.first_page()
    print(p.display_current_page())