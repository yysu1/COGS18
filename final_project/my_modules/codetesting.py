import module1 as mm

def test_remove_punctuation():
    assert isinstance(mm.remove_punctuation('i like cake, chocolate, cookies, and ice-cream'), str)
    assert mm.remove_punctuation('i like cake, chocolate, cookies, and ice-cream')=='i like cake chocolate cookies and ice-cream'

def test_check_if_in_list():
    assert isinstance(mm.check_if_in_list('i like cake, chocolate, cookies, and ice-cream',['cake','banana','tea']), dict)
    assert mm.check_if_in_list('i like cake chocolate cookies and ice-cream',['ice-cream','bagel','tea'])['in_list']==True
    assert mm.check_if_in_list('i like cake chocolate cookies and ice-cream',['ice-cream','bagel','tea'])['item']=='ice-cream'
    assert mm.check_if_in_list('i like coffee and tea',['ice-cream','bagel'])['in_list']==False

