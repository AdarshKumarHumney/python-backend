def test_input(cli_inv,monkeypatch,capsys):
    user_in =  iter(["coke","20.0",20])
    monkeypatch.setattr("builtins.input", lambda _: next(user_in))
    result = cli_inv.addItem()
    cap = capsys.readouterr()
    assert result== True
    assert "coke of 20.0 was successfully added to the inventory" in cap.out
    res_s = cli_inv.searchById(1)
    assert res_s['data'][0]['item_name']=="coke"
    assert res_s['data'][0]['item_quant']==20