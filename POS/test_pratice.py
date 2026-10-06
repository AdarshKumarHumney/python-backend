def test_run(cli_ad,userflow,monkeypatch,capsys):
    res_add =  userflow['adm'].addAdmin("Adarsh","adarsh@gmail.com",112233)
    assert res_add['value']==True
    user_inp = iter(["signin","adarsh@gmail.com","112233","search","adarsh@gmail.com","exit","no"])
    monkeypatch.setattr("builtins.input",lambda _:next(user_inp))
    res_run = cli_ad.run()
    cap = capsys.readouterr()
    assert "Welcome to Admin-Menu page" in cap.out
    assert "Please enter your credentials" in cap.out
    assert "Admin authenticated." in cap.out
    assert "Here is the admin - [{'id': 1, 'name': 'Adarsh', 'email': 'adarsh@gmail.com', 'password': '112233'}]" in cap.out
    assert "Exiting the admin menu" in cap.out
    assert "closing..." in cap.out
    
