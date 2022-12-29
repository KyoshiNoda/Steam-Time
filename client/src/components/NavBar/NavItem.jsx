import React from 'react';

function NavItem(props) {
  return <a href={props.route}>{props.title}</a>;
}

export default NavItem;
