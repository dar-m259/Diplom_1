from praktikum.bun import Bun

class TestBun:
    
    def test_set_bun_name_price(self): 
        bun = Bun('cosmos', 100.5)
        
        assert bun.name == 'cosmos'
        assert bun.price == 100.5

    def test_get_bun_name_returns_name(self):
        bun = Bun('cosmos', 100.5)
        
        assert bun.get_name() == 'cosmos'

    def test_get_bun_price_returns_price(self):
        bun = Bun('cosmos', 100.5)

        assert bun.get_price() == 100.5
