import HomeIcon from '@mui/icons-material/Home';
import TaskIcon from '@mui/icons-material/Task';

type SideBarProps = {
  title: string;
  icon: JSX.Element;
  href: string;
};

export const SideBarData: SideBarProps[] = [
  {
    title: 'Home',
    icon: <HomeIcon fontSize='small' />,
    href: '/',
  },
  {
    title: 'My Tasks',
    icon: <TaskIcon fontSize='small' />,
    href: '/tasks',
  }
];
