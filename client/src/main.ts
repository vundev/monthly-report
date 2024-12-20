import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { ClarityIcons, homeIcon, logoutIcon } from '@cds/core/icon';
import '@cds/core/icon/register.js';
import { AppModule } from './app/app.module';

ClarityIcons.addIcons(homeIcon, logoutIcon);

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch((err) => console.error(err));
