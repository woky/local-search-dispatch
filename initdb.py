import os
from storage import *

#os.system('rm db.sqlite3')

qtps = [
	QueryTemplate(
		name         = 'ABZ slovník českých synonym',
		url_template = 'http://www.slovnik-synonym.cz/web.php/hledat?cizi_slovo=%s',
	),
	QueryTemplate(
		name         = 'ABZ slovník cizích slov',
		url_template = 'http://slovnik-cizich-slov.abz.cz/web.php/hledat?cizi_slovo=%s',
	),
	QueryTemplate(
		name         = 'Add-ons for Firefox',
		url_template = 'https://addons.mozilla.org/en-US/firefox/search/?q=%s',
	),
	QueryTemplate(
		name         = 'ArchWiki',
		url_template = 'https://wiki.archlinux.org/index.php?search=%s',
	),
	QueryTemplate(
		name         = 'AUR',
		url_template = 'https://aur.archlinux.org/packages/?O=0&K=%s',
	),
	QueryTemplate(
		name         = 'DuckDuckGo',
		url_template = 'https://duckduckgo.com/?q=%s',
	),
	QueryTemplate(
		name         = 'Etymology',
		url_template = 'https://www.etymonline.com/word/%s',
	),
	QueryTemplate(
		name         = 'GitHub',
		url_template = 'https://github.com/search?utf8=%E2%9C%93&q=%s',
	),
	QueryTemplate(
		name         = 'Google CS',
		url_template = 'https://www.google.com/search?safe=off&hl=cs&num=50&q=%s',
	),
	QueryTemplate(
		name         = 'Google EN',
		url_template = 'https://www.google.com/search?safe=off&hl=en&num=50&q=%s',
	),
	QueryTemplate(
		name         = 'Google EN Verbatim',
		url_template = 'https://www.google.com/search?safe=off&hl=en&tbs=li:1&num=50&q=%s',
	),
	QueryTemplate(
		name         = 'Google Maps',
		url_template = 'https://www.google.com/maps/search/%s',
	),
	QueryTemplate(
		name         = 'Google Translate',
		url_template = 'https://translate.google.com/#auto/auto/%s',
	),
	QueryTemplate(
		name         = 'Heureka.cz',
		url_template = 'https://www.heureka.cz/?h%5Bfraze%5D=%s',
	),
	QueryTemplate(
		name         = 'HN Search',
		url_template = 'https://hn.algolia.com/?query=%s',
	),
	QueryTemplate(
		name         = 'Mapy',
		url_template = 'https://mapy.cz/zakladni?q=%s',
	),
	QueryTemplate(
		name         = 'Maven Repository',
		url_template = 'https://mvnrepository.com/search.html?query=%s',
	),
	QueryTemplate(
		name         = 'MDN',
		url_template = 'https://developer.mozilla.org/en-US/search?q=%s',
	),
	QueryTemplate(
		name         = 'metacpan',
		url_template = 'https://metacpan.org/search?q=%s',
	),
	QueryTemplate(
		name         = 'Microsoft Docs',
		url_template = 'https://docs.microsoft.com/en-us/search/index?search=%s',
	),
	QueryTemplate(
		name         = 'MSDN',
		url_template = 'https://social.msdn.microsoft.com/Search/en-US?query=%s',
	),
	QueryTemplate(
		name         = 'Netsplit',
		url_template = 'http://irc.netsplit.de/channels/?chat=%s',
	),
	QueryTemplate(
		name         = 'OneLook',
		url_template = 'https://onelook.com/?w=%s',
	),
	QueryTemplate(
		name         = 'Python',
		url_template = 'https://docs.python.org/3/search.html?q=%s',
	),
	QueryTemplate(
		name         = 'Seznam Slovník',
		url_template = 'https://slovnik.seznam.cz/en-cz/?q=%s',
	),
	QueryTemplate(
		name         = 'Seznam.cz',
		url_template = 'https://search.seznam.cz/?q=%s',
	),
	QueryTemplate(
		name         = 'Urban Dictionary',
		url_template = 'https://www.urbanQueryTemplateionary.com/define.php?term=%s',
	),
	QueryTemplate(
		name         = 'Vocabulary.com',
		url_template = 'https://www.vocabulary.com/QueryTemplateionary/%s',
	),
	QueryTemplate(
		name         = 'Wikipedia CS',
		url_template = 'https://cs.wikipedia.org/w/index.php?search=%s',
	),
	QueryTemplate(
		name         = 'Wikipedia EN',
		url_template = 'https://en.wikipedia.org/w/index.php?search=%s',
	),
	QueryTemplate(
		name         = 'Wiktionary',
		url_template = 'https://www.google.com/search?q=%s+site:wiktionary.org',
	),
	QueryTemplate(
		name         = 'Wolfram|Alpha',
		url_template = 'https://www.wolframalpha.com/input/?i=%s',
	),
	QueryTemplate(
		name         = 'YouTube',
		url_template = 'https://www.youtube.com/results?search_query=%s',
	),
	QueryTemplate(
		name         = 'JDK',
		url_template = 'https://duckduckgo.com/?q=site%3Ahttps%3A%2F%2Fdocs.oracle.com%2Fjavase%2F10%2Fdocs%2Fapi+%s',
	),
]

with Storage() as s:
	for qtp in qtps:
		s.tpl_add(qtp)

with Storage() as s:
    for qt in s.tpl_get_all():
        print(qt)
