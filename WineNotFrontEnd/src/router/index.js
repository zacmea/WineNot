import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignUpView from "../views/SignUpView.vue";
import LoginView from "../views/LoginView.vue";
import WineDetailsTile from "../components/WineDetailsTile.vue";
import WineLists from "../components/ListOfCollexns.vue";
import WineListIndexView from "@/views/WineListIndexView.vue";
import ListOfCollexns from "../components/ListOfCollexns.vue";
import CollexnDetail from "../components/CollexnDetail.vue"; // Import the new component
import AboutView from "@/views/AboutView.vue";
import UserProfile from "@/components/UserProfile.vue";
import Search from "@/components/Search.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeView,
        },
        {
            path: "/signup",
            name: "signup",
            component: SignUpView,
        },
        {
            path: "/login",
            name: "login",
            component: LoginView,
        },
        {
            path: "/search", 
            name: "search",
            component: Search,
        },
        {
            path: "/about",
            name: "about",
            component: AboutView,
        },
        {
            path: "/profile",
            name: "profile",
            component: UserProfile,
        },
        {
            path: "/winetile",
            name: "winetile",
            component: WineDetailsTile,
        },
        {
            path: "/collexns",
            name: "collexns",
            component: ListOfCollexns,
        },
        {
            path: "/collexn/:id",
            name: "collexn-detail",
            component: CollexnDetail,
            props: true,
        },
    ],
});

export default router;
