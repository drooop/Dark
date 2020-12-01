import Vue from "vue";
import {
  Button,
  Form,
  FormItem,
  Input,
  Container,
  Aside,
  Main,
  Header,
  Menu,
  MenuItem,
  MenuItemGroup,
  Submenu,
  Breadcrumb,
  BreadcrumbItem,
  Card,
  Row,
  Col,
  Table,
  TableColumn,
  Switch,
  Pagination,
  Dialog,
} from "element-ui";
import { Message } from "element-ui";

Vue.prototype.$message = Message;

Vue.use(Button)
  .use(Form)
  .use(FormItem)
  .use(Input)
  .use(Container)
  .use(Aside)
  .use(Main)
  .use(Header)
  .use(Menu)
  .use(MenuItem)
  .use(MenuItemGroup)
  .use(Submenu)
  .use(Breadcrumb)
  .use(BreadcrumbItem)
  .use(Card)
  .use(Row)
  .use(Col)
  .use(Table)
  .use(TableColumn)
  .use(Switch)
  .use(Pagination)
  .use(Dialog);
