import React from 'react';
import NavItem from './NavItem';
function NavBar() {
  return (
    <div className="navbar bg-base-100">
      <div className="flex-1">
        <a href="/" className="btn btn-ghost normal-case text-xl">
          SteamTime
        </a>
      </div>
      <div className="flex-none">
        <ul className="menu menu-horizontal px-1">
          <li>
            <NavItem title="Timer" route="/Timer" />
          </li>
          <li>
            <NavItem title="Statistics" route="/Statistics" />
          </li>
          <li tabIndex={0}>
            <a href='/Settings'>
              Settings
            </a>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default NavBar;
