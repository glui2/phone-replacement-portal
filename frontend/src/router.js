import Vue from "vue";
import Router from "vue-router";
import Triage from "./views/singleHandsetFaultsView.vue";
import OrderReplacement from "./views/orderReplacementPartView.vue";
import Welcome from "./views/landingPageView.vue";
import HowtoGuides from "./views/howtoGuidesView.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "Welcome",
      component: Welcome
    },
    {
      path: "/singlehandsettriage",
      name: "Single Handset Triage",
      component: Triage
    },
    {
      path: "/orderreplacement/orderpart/:partNumberProp",
      name: "Order Specified Replacement Part",
      component: OrderReplacement,
      props: true
    },
    {
      path: "/orderreplacement",
      name: "Order Replacement Part",
      component: OrderReplacement,
      props: false
    },
    {
      path: "/howtoguides",
      name: "How-To Guides",
      component: HowtoGuides,
      props: false
    }
  ]
});
