import upperFirst from 'lodash/upperFirst';
import camelCase from 'lodash/camelCase';

// import { LANGUAGES } from '../constants';

function pascalCase(str: string) {
  return upperFirst(camelCase(str));
}

function titleize(hyphenedString: string): string {
  return upperFirst(hyphenedString.split('-').join(' '));
}

export interface Page {
  pathname: string;
  subheader?: string;
  title?: string | false;
}

export function pageToTitle(page: Page): string | null {
  if (page.title === false) {
    return null;
  }

  if (page.title) {
    return page.title;
  }

  const path = page.subheader || page.pathname;
  const name = path.replace(/.*\//, '').replace('react-', '').replace(/\..*/, '');

  // TODO remove post migration
  if (path.indexOf('/api-docs/') !== -1) {
    return pascalCase(name);
  }

  // TODO support more than React component API (PascalCase)
  if (path.indexOf('/api/') !== -1) {
    return pascalCase(name);
  }

  return titleize(name);
}

export type Translate = (id: string, options?: Partial<{ ignoreWarning: boolean }>) => string;

export function pageToTitleI18n(page: Page, t: Translate): string | null {
  const path = page.subheader || page.pathname;
  return t(`pages.${path}`, { ignoreWarning: true }) || pageToTitle(page);
}

/**
 * Get the value of a cookie
 * Source: https://vanillajstoolkit.com/helpers/getcookie/
 * @param name - The name of the cookie
 * @return The cookie value
 */
export function getCookie(name: string): string | undefined {
  if (typeof document === 'undefined') {
    throw new Error(
      'getCookie() is not supported on the server. Fallback to a different value when rendering on the server.',
    );
  }

  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) {
    return parts[1].split(';').shift();
  }

  return undefined;
}

/**
 * as is a reference to Next.js's as, the path in the URL
 * pathname is a reference to Next.js's pathname, the name of page in the filesystem
 * https://nextjs.org/docs/api-reference/next/router
 */
export function pathnameToLanguage(pathname: string): {
  canonicalAs: string;
  canonicalPathname: string;
} {
  const canonicalAs = pathname;
  const canonicalPathname = canonicalAs
    .replace(/^\/api/, '/api-docs')
    .replace(/#(.*)$/, '')
    .replace(/\/$/, '');

  return {
    canonicalAs,
    canonicalPathname,
  };
}

export function escapeCell(value: string): string {
  // As the pipe is use for the table structure
  return value.replace(/</g, '&lt;').replace(/`&lt;/g, '`<').replace(/\|/g, '\\|');
}