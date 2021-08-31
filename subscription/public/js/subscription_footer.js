

frappe.Application = Class.extend({
	startup: function() {
		let menu = document.getElementById('page-Workspaces');
		let foot = document.createElement('footer');
		foot.innerHTML = "<div role=\"navigation\" class=\"upgrade-bar\" id=\"Subscription\" style=\"bottom: 0px;position: fixed;background-color: #f9f5e3;border: 1px solid #d1d8dd;z-index: 1;border-radius: 0;text-align: center;width: 100%;\">  <div class=\"container\"><p>You have <b>1</b> day remaining in your subscription. </p></div></div> "
		menu.insertBefore(foot, menu.firstElementChild.nextSibling);
	}
})