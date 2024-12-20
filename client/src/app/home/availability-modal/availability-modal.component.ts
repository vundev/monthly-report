import { Component, Input, OnInit } from '@angular/core';
import { AvailabilityLevel } from './availability.model';
import { ModalService } from 'src/app/modal/modal.service';
import { AvailabilityService } from './availability.service';

@Component({
  selector: 'availability-modal',
  templateUrl: 'availability-modal.component.html',
  styleUrls: ['availability-modal.component.scss'],
})
export class AvailabilityModalComponent implements OnInit {
  readonly defaultAvailabilityLevel = AvailabilityLevel.DEFAULT;
  readonly customerSpecificAvailabilityLevel =
    AvailabilityLevel.CUSTOMER_SPECIFIC;
  readonly expiredAvailabilityLevel = AvailabilityLevel.EXPIRED;

  @Input()
  tenant_id!: number;

  @Input()
  tenant_email!: string;

  selectedLevel: AvailabilityLevel = AvailabilityLevel.DEFAULT;

  constructor(
    private modalService: ModalService,
    private availabilityService: AvailabilityService
  ) {}

  ngOnInit(): void {}

  submit() {
    this.availabilityService
      .logAvailabilityChangeMessage$({
        tenant_id: this.tenant_id,
        level: this.selectedLevel,
      })
      .subscribe(() => this.modalService.close());
  }

  close() {
    this.modalService.close();
  }
}
