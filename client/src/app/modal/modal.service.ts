import {
  Injectable,
  ComponentFactoryResolver,
  Injector,
  ApplicationRef,
  ComponentRef,
  Type,
} from '@angular/core';
import { ModalWrapperComponent } from './modal-wrapper.component';

@Injectable({
  providedIn: 'root',
})
export class ModalService {
  private modalRef: ComponentRef<ModalWrapperComponent> | null = null;

  constructor(
    private componentFactoryResolver: ComponentFactoryResolver,
    private injector: Injector,
    private appRef: ApplicationRef
  ) {}

  open<T>(
    component: Type<T>,
    inputs?: Partial<T>,
    options?: { title?: string; size?: 'sm' | 'lg' | 'xl' }
  ) {
    if (this.modalRef) {
      return;
    }

    // Create the modal wrapper
    const modalFactory = this.componentFactoryResolver.resolveComponentFactory(
      ModalWrapperComponent
    );
    this.modalRef = modalFactory.create(this.injector);

    // Set wrapper properties
    const { title = 'Modal Title', size = 'lg' } = options || {};
    this.modalRef.instance.title = title;
    this.modalRef.instance.size = size;
    this.modalRef.instance.isOpen = true;
    this.modalRef.instance.onCloseModal = () => {
      this.close();
    };

    // Attach the modal wrapper to the application
    this.appRef.attachView(this.modalRef.hostView);
    document.body.appendChild((this.modalRef.hostView as any).rootNodes[0]);

    // Dynamically load the child component into the modal
    const childFactory =
      this.componentFactoryResolver.resolveComponentFactory(component);
    const childRef =
      this.modalRef.instance.contentHost.createComponent(childFactory);

    // Apply inputs to the child component
    if (inputs) {
      Object.assign(<any>childRef.instance, inputs);
    }
  }

  close(): void {
    if (this.modalRef) {
      this.dispose();
    }
  }

  private dispose() {
    this.appRef.detachView(this.modalRef!.hostView);
    this.modalRef!.destroy();
    this.modalRef = null;
  }
}
