def test_product_has_inventory(dummy_product):
    assert dummy_product['stock']>=1