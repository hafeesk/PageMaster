from __future__ import unicode_literals
import frappe

def get_context(context):
	#body
	#---------------
	# -->Background-Image
	context.bodyimage = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Body Settings'", as_dict=True)[0].value == "Image":
		context.bodyimage = True
		context.bodyimagesource = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_img' AND doctype = 'Body Settings'", as_dict=True)
		
	# -->Background-Color
	context.bodycolor = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_select' AND doctype = 'Body Settings'", as_dict=True)[0].value == "Color":
		context.bodycolor = True
		context.bodycolorcode = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'bg_color' AND doctype = 'Body Settings'", as_dict=True)
		
	#navbar
	#---------------------
	context.navbar = True
	context.nav_bg_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'nav_bg_color' AND doctype = 'Navbar'", as_dict=True)[0].value
	context.nav_txt_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'nav_txt_color' AND doctype = 'Navbar'", as_dict=True)[0].value
	context.navlinks = frappe.db.sql("SELECT title, link FROM `tabNavbar Item` WHERE parent = 'Navbar' ORDER BY idx ASC", as_dict=True)
	
	#footer
	#-------------------
	context.footer = True
	context.footer_bg_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_bg_color' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.footer_txt_color = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'footer_txt_color' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.txt = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'txt' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.link_title = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'link_title' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
	context.link = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'link' AND doctype = 'PageMaster Footer'", as_dict=True)[0].value
		
	#timeline
	#-----------------------
	context.timeline = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_timeline' AND doctype = 'About Us'", as_dict=True)[0].value == "1":
		context.timeline = True
		timeline_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'About Us' AND field = 'timeline'", as_dict=True)[0].value
		context.timeline_intro = frappe.db.sql("SELECT timeline_intro FROM `tabTimeline Set` WHERE title = '"+timeline_parent+"'", as_dict=True)[0].timeline_intro
		context.timelines = frappe.db.sql("SELECT year, highlight, align FROM `tabTimeline` WHERE parent = '"+timeline_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#cards
	#--------------------------
	context.card = False
	if frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'incl_cards' AND doctype = 'About Us'", as_dict=True)[0].value == "1":
		context.card = True
		card_parent = frappe.db.sql("SELECT value FROM `tabSingles`WHERE doctype = 'About Us' AND field = 'cards'", as_dict=True)[0].value
		context.cards = frappe.db.sql("SELECT img_or_fa, card_fa, card_fa_size, link_linkedin, card_img, title, link_twitter, subtitle_1, subtitle_2, btn_link, link_facebook, btn_title FROM `tabPage Cards` WHERE parent = '"+card_parent+"' ORDER BY idx ASC", as_dict=True)
		
	#introduction
	context.intro = frappe.db.sql("SELECT value FROM tabSingles WHERE field = 'introduction' AND doctype = 'About Us'", as_dict=True)[0].value